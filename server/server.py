from flask import Flask, render_template, Response, jsonify, request, json
from flask_cors import CORS
from ner import NER

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
    text = "Annepu Sai Charan +91 9849659113 | saicharan0662@gmail.com | https://www.linkedin.com/in/saicharan0662/ | https://github.com/Saicharan0662 | LeetCode | GeeksForGeeks Education Indian Institute of Information Technology Senapati, Manipur Imphal, India Bachelor in Technology in Computer Science and Engineering — CPI:7.96 Dec 2020 – May 2024 Course work : Operating system, Computer networks, Object oriented programming and DBMS Experience FOSSEE Summer Intern May 2023 – Present Indian Institute of Technology Bombay (IIT-B) Mumbai/Hybrid • Developing “Osdag on Cloud,” an impactful open-source initiative revolutionizing structural design and analysis. • Building robust web application using react.js, Django and PostgreSQL database. Software Engineer Intern May 2022 – May 2023 Artyvis Remote • Engineered an automated homepage and connected pages system using React.js, with intelligent rendering and styling for 25% reduced development effort. • Implemented scalable, persistent filters, reducing bounce rates by 20%. • Migrated product to Next.js, reducing initial load time by 40% and increasing user clicks through rates by 90%. • Revamped front-end architecture to drastically reduce API calls by an impressive 60%. • Facilitated seamless personalization through wish-list feature, increase in 25% click through rates on products. • Participated in each step of product development process for features reaching over 130,000+ users. Software Development Intern (React.js) June 2021 – October 2021 Infokriti Remote • Did the API integration for multi-page forms and user data, resulting in user data errors by 30% and increasing form completion rate by 20%. • Crafted optimized UI components, resulted 20% decrease in bounce rate. • Designed multiple pages using React and tailwind CSS that works across desktop, tablets and 10+ other devices. Projects Online Examination | React.js, Node.js, Flask, MongoDB, Open-CV, Python GitHub • A full stack, examination portal for creating and attending exams and viewing summaries. • Set timer for exams; auto-submits when timer goes off. • Developed a browser tab monitoring system, resulting in a 100% improvement in exam security and integrity. • OpenCV face detection model integrated with Flask to track head movements, duration of head hold positions, and user status when leaving camera frame, with the accuracy of 90%. Data updated regularly. • Examiner can generate MCQ’s using a web doc link, saves the 80% time; used “name entity recognition” technique. Job Tracker | React.js, Node.js, MongoDB GitHub • Created a tool for job application management, leading to a 60% increase in productivity. • Implementation of secure authentication and authorization. • Designed a seamless and intuitive UI/UX for easy navigation and functionality. • Enabled users to perform CRUD operations for efficient job management. Skills Programming Languages : C, C++ (full proficiency), JavaScript(proficient), Python(proficient), HTML, CSS, SQL. Frameworks : React, Next.js, Node.js, Express.js, Django. Databases : MongoDB, MySQL Other skills : Git, GitHub, Data Structures, Algorithms, Agile, team player. Achievements • Cleared “Advance Distributed Systems” certification of NPTEL with rank 1 in institute. • Secured runner-up position in MongoDB charts challenge among 100s of participants. • Invited as a virtual guest speaker (virtual) at RTU for a Git workshop with 300+ attendees. • Secured a rank under 5000 in Google Kick Start 2022."

    global ner
    ner = NER(text)

    formated_text_output = ner.get_formated_text()
    # print(formated_text_output)

    return jsonify(result=formated_text_output, success=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True,
            use_reloader=False, debug=True)
