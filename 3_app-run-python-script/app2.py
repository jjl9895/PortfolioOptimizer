import os
import gradio as gr
import time

def get_responses(question):
    # Initialize status messages
    status = []

    # Step 1: Simulate loading from the database
    status.append("Loading from database of the latest news")
    yield status[-1]  # Yield the first status message
    time.sleep(1)  # Simulate time delay for database loading

    # Step 2: Done loading from vector database
    status.append("Done loading news from vector database")
    yield status[-1]  # Yield the second status message
    time.sleep(1)  # Simulate time delay

    # Step 3: LLM advisor is thinking
    status.append("LLM advisor is thinking")
    yield status[-1]  # Yield the third status message
    time.sleep(2)  # Simulate LLM processing time

    # Step 4: LLM advisor is done thinking
    status.append("LLM advisor is done thinking")
    yield status[-1]  # Yield the final status message

    # Final response
    response_1 = (
        "Hello"
    )

    # Yield the final response after all status updates are shown
    yield response_1

def main():
    # Configure Gradio app with Textbox and Button
    print("Configuring Gradio app")
    
    with gr.Blocks() as demo:
        with gr.Column():  # Ensures vertical stacking
            question_input = gr.Textbox(label="Financial Advisor Prompt", placeholder="Enter your question here")
            response_output = gr.Textbox(label="LLM Recommendation")
            submit_button = gr.Button("Submit")
        
        submit_button.click(fn=get_responses, inputs=question_input, outputs=response_output)

    # Launch Gradio app
    print("Launching Gradio app")
    demo.launch(
        share=True,
        show_error=True,
        server_name='127.0.0.1',
        server_port=8080
    )
    print("Gradio app ready")

if __name__ == "__main__":
    main()
