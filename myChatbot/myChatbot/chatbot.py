
import google.generativeai as genai

genai.configure(api_key="AIzaSyBjeSsNMiXbnpX4r2k9zvYRXgULBdMYzKE")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)
 
def get_ai_answer(query):
    info = """
    The DHQ Hospital Kotli is located in district Kotli, Azad Kashmir. It offers a variety of specialists for various medical needs.  For internal medicine, you can see Dr. Yawar on Mondays and Thursdays, Dr. Draeed Yossaf on Tuesdays, Dr. Fasil on Fridays, and Dr. Jahangir Ch. on Saturdays.  Gynecological care is available with Dr. Shar Nasarullah on Mondays and Thursdays, Dr. Shabnam on Tuesdays and Fridays, Dr. Insabat on Wednesdays, and Dr. Refaat on Saturdays.  Ophthalmology services are provided by Dr. Khalid Usman on Mondays and Wednesdays, and Dr. Nazir on Tuesdays and Thursdays.  In case of orthopedic issues, Dr. Safeer is available on Mondays and Wednesdays, while Dr. Sajid Manzoor sees patients on Tuesdays and Thursdays.  For neurological surgery, Dr. Abdul Ghafoor Raja can be consulted on Mondays and Thursdays.  Finally, child specialist Dr. Rashid Shamsi is available for pediatric care on Mondays and Thursdays.  Remember, this is just a general schedule and it's always best to call the hospital beforehand to confirm availability and make appointments.

      """
    final_query = {f"the data is {info} and here is question {query}\n now please give me answer from given data not from your own info. just answer on a single paragraph.if you could't found answer in given data then reply i can't assit with you"}
    response = chat_session.send_message(final_query)
    return response.text
