import os
import openai

#openai.api_key = os.environ["OPENAI_API_KEY"]
def test_openai_api():
    # Remplacez 'your-api-key' par votre clé API OpenAI
    openai.api_key = os.environ["OPENAI_API_KEY"]

    try:
        # Utilisez l'API pour générer un court texte avec gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, how are you?"}
            ]
        )
        print("L'installation de OpenAI est réussie !")
        print("Réponse de l'API :", response.choices[0].message['content'].strip())
    except Exception as e:
        print("Erreur lors de l'utilisation de l'API OpenAI :", e)

if __name__ == "__main__":
    test_openai_api()