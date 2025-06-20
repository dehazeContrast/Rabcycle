import './CaptureBtn.css'

//call to send picture towards the backend to classify image

function capturePhoto() {
    const context = canvas.getContext("2d");

    if (width && height) {
        canvas.width = innerWidth;
        canvas.height = innerHeight;
    }
}

const CaptureBtn = () => {
    const clickUpdate = () => {
        console.log('Photo captured.')
           
    };
    return (
        <div>
            <button className="capture-btn">
                Snapshot
            </button>
        </div>

    );
};

export default CaptureBtn;

