
import openai

class GPT:
    def __init__(self):
        # Ініціалізація OpenAI GPT-3.5
        self.api_key = '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'  # Замініть на свій API-ключ OpenAI

    def request(self, prompt):
        openai.api_key = self.api_key

        # Виклик OpenAI GPT-3.5 API для отримання відповіді на запитання
        response = openai.Completion.create(
            engine='text-davinci-003',  # Виберіть відповідний двигун
            prompt=prompt,
            max_tokens=50,  # Максимальна кількість токенів в відповіді
            temperature=0.7,  # Контроль випадковості відповідей (значення від 0 до 1)
            n=1,  # Кількість варіантів відповідей
            stop=None,  # Рядок, який вказує на зупинку генерації тексту
            timeout=15  # Максимальний час очікування (в секундах)
        )

        if response and 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['text']
        else:
            return "На жаль, не вдалося отримати відповідь."