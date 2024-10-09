import os
import gradio as gr

def get_responses(question):
    # Example function for processing the question (You can replace this with your actual logic)
    response_1 = f"Response to '{question}' without context."
    response_2 = f"Response to '{question}' with context (RAG)."
    return response_1, response_2

def main():
    # Configure Gradio app with Textbox and Button
    print("Configuring Gradio app")
    demo = gr.Interface(
        fn=get_responses,
        inputs=gr.Textbox(label="Question", placeholder="Enter your question here"),
        outputs=[gr.Textbox(label="Asking LLM with No Context"), gr.Textbox(label="Asking LLM with Context (RAG)")],
        live=False,  # Ensures the function is triggered with a button press
    )

    # Launch Gradio app
    print("Launching Gradio app")
    demo.launch(
        share=True,
        enable_queue=True,
        show_error=True,
        server_name='127.0.0.1',
        server_port=int(os.getenv('CDSW_APP_PORT'))
    )
    print("Gradio app ready")

if __name__ == "__main__":
    main()
