import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    print("Content fetched successfully")
else:
    print("Failed to fetch the page")
    exit()

parsed_html = BeautifulSoup(html_content, "html.parser")

question_title = parsed_html.find("a", class_="question-hyperlink").text.strip()
print(f"Question Title: {question_title}\n")
question_body = parsed_html.find("div", class_="s-prose js-post-body").text.strip()
print(f"Question Body: {question_body}\n")

formatted_output = f"Question:\n{question_title}\n\nDetails:\n{question_body}\n\n"

answer = parsed_html.find_all("div", class_="s-prose js-post-body")

formatted_output += "Answers:\n\n"

for idx, answer in enumerate(answer[1:], start=1):  
    answer_text = answer.text.strip()
    formatted_output += f"Answer {idx}:\n{answer_text}\n{'-'*50}\n"

print(formatted_output)

output_file = "answers.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(formatted_output)

print(f"Data written to {output_file}")