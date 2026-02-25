import streamlit as st
from story_generator import generate_story
from image_generator import generate_image
from pdf_builder import create_pdf

st.title("📚 FableForge - AI Picture Book Creator")

prompt = st.text_input("Enter your story idea")

if st.button("Generate Book"):
    if not prompt:
        st.warning("Please enter a prompt.")
        st.stop()

    story = generate_story(prompt)

    images = []

    for page in story["pages"]:
        st.subheader(f"Page {page['page_number']}")
        st.write(page["text"])

        image_path = generate_image(page["image_prompt"], page["page_number"])
        st.image(image_path)
        images.append(image_path)

    pdf_path = create_pdf(story, images)

    with open(pdf_path, "rb") as f:
        st.download_button("Download PDF", f, file_name="fableforge_book.pdf")
