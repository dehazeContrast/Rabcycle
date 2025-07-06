const video = document.querySelector(".video");
const cameraButton = document.querySelector(".capture-btn");
const canvas = document.querySelector(".canvas");
const context = canvas.getContext("2d");
//Calls the video and caemra button(capture)

navigator.mediaDevices.getUserMedia({video: true})
.then(stream => {
    video.srcObject = stream;
    video.play();
})
//This is a call that brings it together, which basically is 
//saying make the live feed from the video continue until the 
//user takes a photo and then just snap that specific frame
//of the photo and end the live feed

cameraButton.addEventListener("click", () => {
    video.classList.toggle("effect");
    setTimeout(() => video.classList.toggle("effect"), 400);

    //Matches the frame to the video size 
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    let image_data_url = canvas.toDataURL("image/jpeg");

    //Downloads the image directly to the computer 
    const downloadLink = document.createElement("a")
    downloadLink.href = image_data_url
    downloadLink.download = "plastic.jpeg"
    document.body.appendChild(downloadLink)
    downloadLink.click();
    document.body.removeChild(downloadLink);
})