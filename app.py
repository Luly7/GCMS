import gradio as gr
from utils.processing import (
    run_prediction, generate_plot, run_training, zip_results, list_all_files
)

with gr.Blocks() as demo:
    gr.Markdown("## 🧪 GCMSFormer iBot – Predict, Train, Explore")

    with gr.Tab("🔍 Prediction"):
        mzml_input = gr.File(label="Upload .mzML")
        smi_input = gr.File(label="Upload .smi")
        predict_btn = gr.Button("Run Prediction")
        pred_output = gr.Textbox(label="Output")
        predict_btn.click(run_prediction, [mzml_input, smi_input], pred_output)

    with gr.Tab("📈 Chromatogram Plot"):
        plot_btn = gr.Button("Plot Chromatogram")
        plot_output = gr.Plot()
        plot_btn.click(generate_plot, [], plot_output)

    with gr.Tab("🧠 Train Model"):
        train_btn = gr.Button("Train")
        train_output = gr.Textbox()
        train_btn.click(run_training, [], train_output)

    with gr.Tab("📥 Download Results"):
        zip_btn = gr.Button("Create ZIP")
        file_output = gr.File()
        zip_btn.click(zip_results, [], file_output)

    with gr.Tab("📁 File Browser"):
        list_btn = gr.Button("List Files")
        list_output = gr.Textbox(lines=10)
        list_btn.click(list_all_files, [], list_output)

demo.launch(share=True, debug=True)
