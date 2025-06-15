import google.generativeai as genai
import flow
import detect_intent

class GeminiChatbot:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=f"""
                            You are an AI assistant inside the HireNy platform.

                            You help job seekers and recruiters with:
                            - Job applications
                            - CV writing
                            - Interview scheduling
                            - Course recommendations
                            - Salary insights

                            Use real-time data passed in the prompt if available. If not, rely on your general knowledge.
                             If a user asks for private info (like application status), tell them to check their dashboard.
                             
                             and these {flow.task_flows} are the most common flows in the system if user wants to know how do something
                            """
        )
        self.chat = self.model.start_chat(history=[])

    def get_response(self, user_input):
        # intent = detect_intent.detect_intent(user_input)
        # task_guide = flow.task_flows.get(intent)
        #
        # if task_guide:
        #     prompt = f"""
        #         User asked: {user_input}
        #
        #         Here’s how to do that on the HireNy platform:
        #
        #         {task_guide}
        #         """
        # else:
        # prompt = user_input

        response = self.chat.send_message(user_input)
        return response.text
