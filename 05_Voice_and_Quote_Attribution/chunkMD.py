import os

def chunk_markdown_by_lines(input_file, output_dir, lines_per_chunk=750):
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_chunks = (len(lines) + lines_per_chunk - 1) // lines_per_chunk

    for i in range(total_chunks):
        chunk_lines = lines[i * lines_per_chunk:(i + 1) * lines_per_chunk]
        chunk_path = os.path.join(output_dir, f"chunk_{i+1:02d}.md")
        with open(chunk_path, "w", encoding="utf-8") as out:
            out.writelines(chunk_lines)

    print(f"✅ Split into {total_chunks} chunks in '{output_dir}'")

# Example usage
chunk_markdown_by_lines("full_conversation.md", "conversation_chunks", lines_per_chunk=750)
