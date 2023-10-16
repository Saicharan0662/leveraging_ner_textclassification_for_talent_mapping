from flask import Flask, render_template, Response, jsonify, request, json
from flask_cors import CORS
from ner import NER

import re

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'I am your super flask server'


@app.route('/format_text', methods=['GET'])
def format_text():
    # req = request.get_data()
    # req = json.loads(req)
    # text = req['text']
    text = "Last Updated on 6th September 2023 Ritu Raj Choudhary rchoudhary@iiitmanipur.ac.in || +918696314631 || Portfolio EDUCATION IIITM Computer Science Engineering B-TECH : Final year : 7.8 CGPA 2020 - 2024 Imphal,Manipur IN SKILLS CYBER SECURITY Experienced: • Bug Hunting • Penetration Testing • Ethical Hacking • API security • SIME / SOC • Networking • Automation • API security SOFTWARE Experienced: • Developement • APIs • Performance • QA testing • Selinum • Postman PROGRAMMING Experienced: • DSA • C/C++ • Bash • Python • HTML/CSS/JavaScript/ MACHINE LEARNING Research Project TOOLS || APPLICATIONS • Burpsuite • NMap • Wireshark • Nessus • Metasploit • Eclipse • Postman • Apache Jmeter CERTIFICATION • CCNA • Microsoft- MTA Security • AZ-900 / AI-900 • CISCO -Cyber security Essentials AWARDS • CSI CYBER SECURITY AWARD 2023 , IIT Bombay • PROUD OF CITY AWARD • LET'S INSPIRE BIHAR AWARD By: IPS Vikas Vaibhav. EXPERIENCE RESEARCH INTERNSHIP | IIT Ropar , Punjab Since May 2023 | Aug 2023 RESEARCH INTERNSHIP | Edinburgh Napier University, Scotland , UK • Working on a research paper for Malware Detection and IDS using Deep learning (Machine Learing) for edege based IOT devices. INTERN | Artyvis PVT Since-Feb 2022 | WFH • It is product based startup Working as a Automation testing , Performance testing , Code analysis , Security, QA testing, Manual testing. CYBER SECURITY INTERN | Solar Industy PVT July 2022 – June 2022 | WFM • Worked as VAPT in DART team . • Secured their 18+ module and write reports for POC and Mitigation. GENERAL SECRETARY | IIITM Since-Sept 2022 | Imphal, Manipur • Elected as a General Secretary for Techinical Board in Gymkhana Council. PENETRATION TESTING. | Bug Bounty Hunter From Dec 2021 - Dec 2022 | FreeLancer • Worked as a bug bounty hunter and helped more than 30+ companies to enhance their security and help in mitigation the Security flaws. • EX- Google , Nykaa , Cisco , Indiamart , etc, Got hall of fame , swags, Bounties.. EDUCATOR | Build my project Sep2021- July2022 | Imphal, Manipur • Speaker for multiple workshop and conducted classes for ethical hacking. is also conducted internationally. PROJECT • DEVELOPING FREE TOOLS ALL IN ONE WEBSITE UNDER THE SUPERVISION OF DR. NAVANATH. Project Link: Link: https://thetiss.com . • DEVELOPED SELF-MADE AUTOMATED TOOLS FOR LINUX. Project Link: Link: https://github.com/choudharyrajritu1/Kali . ACKNOWLEDGE • Got an offer from Josh talk for shoot and interview • Given 6+ live interviews in Indian national channels like (ABP News, Sach TAk , Bihar Jharkhand, Aaj tak , Lallantop, etc) • Speaker for Many of the Workshop , Podcast in Organisation like Wollongong University Australia , CANARA Bank • Google Hall of Fame • Lead for Google Devlopers Clubs in cyber security also mentor for of 200+ students guiding for cyber security 1"
    text = re.sub(r'●', '.', text)
    text = re.sub(r'○', '.', text)
    text = re.sub(r'•', '.', text)
    global ner
    ner = NER(text)

    formated_text_output = ner.get_formated_text()
    # print(formated_text_output)

    return jsonify(result=formated_text_output, success=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True,
            use_reloader=False, debug=True)
