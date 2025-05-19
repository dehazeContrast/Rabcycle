
import { useEffect, useRef } from "react";

//creating camera input part
const CameraInput = () => {
    const videoRef = useRef<HTMLVideoElement | null>(null);

//  create react hook for accessing the camera
    useEffect(() => {
    // global created variables
    const constraints = {
        audio: false,
        video: true,
    };

    navigator.mediaDevices
        .getUserMedia(constraints)
        .then((stream) =>  {
            const videoTracks = stream.getVideoTracks();
            console.log("Got stream with constraints:", constraints);
            console.log(`Using video device: ${videoTracks[0].label}`);
            stream.onremovetrack = () => {
                console.log("Stream ended");
            }
            if (videoRef.current) {
                videoRef.current.srcObject = stream;
            }

        })
        .catch((error) => {
            if (error.name === "OverconstrainedError") {
                console.error(
                    `The resolution 
            ${constraints.video.width.exact}x${constraints.video.height.exact}
            px is not supported by your device.`,
                );
            } else if (error.name === "NotAllowedError") {
                console.error(
                    "You need to grant this page permission to access your camera.",
                );
            } else {
                console.error(`getUserMedia error: ${error.name}`, error);
            }
        });
    }, []);

    return (
        <div>
            <video ref={videoRef} autoPlay playsInline />
        </div>
    );
};
    

    
export default CameraInput;