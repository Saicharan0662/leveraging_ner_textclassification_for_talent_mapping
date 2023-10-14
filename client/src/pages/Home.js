import React, { useState } from "react";
import { pdfjs } from 'react-pdf';

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
    'pdfjs-dist/build/pdf.worker.min.js',
    import.meta.url,
).toString();

const Home = () => {
    const [text, setText] = useState("")

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

            setText(extractedText);
        } catch (error) {
            console.error("Error loading or extracting text from PDF:", error);
        }
    }

    return (
        <div>
            <h1>Resume Classifier</h1>
            <div>
                <input type="file" id='pdf-input' onChange={(e) => handleChange(e)} />
                <div>
                    {text && text}
                </div>
            </div>
        </div>
    )
}

export default Home