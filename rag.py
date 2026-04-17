import numpy as np

def retrieve_best_chunk(question, chunks, index, model):
    question_embedding = model.encode([question])
    question_embedding = np.array(question_embedding)

    D, I = index.search(question_embedding, k=1)

    return chunks[I[0][0]]