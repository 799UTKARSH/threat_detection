document.getElementById('threatForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const inputData = document.getElementById('inputData').value;
    const fileInput = document.getElementById('fileInput').files[0];

    let formData = new FormData();
    formData.append('inputData', inputData);
    if (fileInput) {
        formData.append('file', fileInput);
    }

    const response = await fetch('/detect', {
        method: 'POST',
        body: formData,
    });

    const result = await response.json();
    document.getElementById('result').innerHTML = `<div class="alert alert-${result.type}">${result.message}</div>`;
});
