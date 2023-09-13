import fs from 'fs';

function displayFileContent() {
    const content = fs.readFileSync('./file-data.txt', 'utf-8');
    console.log(content);
}

export default displayFileContent;
