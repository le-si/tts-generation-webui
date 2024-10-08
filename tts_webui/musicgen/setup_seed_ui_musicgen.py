import gradio as gr


def setup_seed_ui_musicgen():
    gr.Markdown("Seed")
    with gr.Row():
        seed_input = gr.Number(value=-1, show_label=False, container=False)
        set_random_seed_button = gr.Button(
            "backspace", elem_classes="btn-sm material-symbols-outlined", size="sm"
        )

        set_random_seed_button.click(
            fn=lambda: gr.Number(value=-1), outputs=[seed_input]
        )

        set_old_seed_button = gr.Button(
            "repeat", elem_classes="btn-sm material-symbols-outlined", size="sm"
        )

        def link_seed_cache(seed_cache):
            set_old_seed_button.click(
                fn=lambda x: gr.Number(value=x),
                inputs=seed_cache,
                outputs=seed_input,
            )

    return seed_input, set_old_seed_button, link_seed_cache
