import React, { useState } from "react";
import { pdfjs } from 'react-pdf';
import { PieChart } from 'react-minimal-pie-chart';

const title_list = ['backend development', 'cloud engineer', 'cyber security', 'frontend development', 'machine learning']
const color_list = ['purple', 'red', 'cyan', 'orange', 'green']

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
    'pdfjs-dist/build/pdf.worker.min.js',
    import.meta.url,
).toString();

const Home = () => {
    // const [text, setText] = useState("")
    const [outputs, setOutputs] = useState(null)

    const handleChange = e => {
        var file = document.getElementById('pdf-input').files[0]
        if (!file) return;

        let fr = new FileReader()
        fr.readAsDataURL(file)
        fr.onload = () => {
            let res = fr.result;
            console.log(res)
            extractText(res)
        }
    }

    const extractText = async (base64DataUri) => {
        try {
            const pdfData = atob(base64DataUri.split(",")[1]);
            const dataArray = new Uint8Array(pdfData.length);
            for (let i = 0; i < pdfData.length; i++) {
                dataArray[i] = pdfData.charCodeAt(i);
            }
            const pdf = await pdfjs.getDocument(dataArray).promise;

            let extractedText = "";
            for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
                const page = await pdf.getPage(pageNum);
                const pageText = await page.getTextContent();

                pageText.items.forEach((item) => {
                    extractedText += item.str + " ";
                });
            }

            // setText(extractedText);
            sendTextToServer(extractedText);
        } catch (error) {
            console.error("Error loading or extracting text from PDF:", error);
        }
    }

    const sendTextToServer = async (text) => {
        try {
            const response = await fetch('http://127.0.0.1:5000/format_text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });

            if (!response.ok) {
                throw new Error('Failed to send extracted text to the server');
            }

            const result = await response.json();
            setOutputs(result.predictions)
            console.log('Server response:', result);
        } catch (error) {
            console.error('Error sending extracted text to server:', error);
        }
    };

    return (
        <div>
            <h1>Resume Classifier</h1>
            <div className="container">
                <input type="file" id="pdf-input" onChange={(e) => handleChange(e)} />

                <div class="chart-container">
                    {outputs && <PieChart
                        data={outputs}
                        animate={true}
                        labelStyle={{
                            fontSize: "12px",
                            fontWeight: 'bold',
                            color: '#333',
                        }}
                    />}
                </div>

                <div class="colormap">
                    {title_list.map((title, index) => (
                        <div class="colormap-item">
                            <div class="colormap-color" style={{ backgroundColor: color_list[index] }}></div>
                            {title}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Home