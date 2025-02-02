import SwiftUI
import AVFoundation

struct ContentView: View {
    var body: some View {
        NavigationStack {
            CameraView()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

// The preview for the camera  
struct CameraView: View 
{
    @StateObject var camera = CameraModel()
    var body: some View
    {

        ZStack
        {
            CameraPreivew(camera: camera)
                .ignoreSafeArea(.all, edges: .all) 
            VStack {
                Image("imgs/grass.png")
                    .resizable()
                    .scaledToFit()
                    .frame(maxWidth: .infinity)
                    .frame(height: 368)
            }
        }

        VStack 
        {
            if camera.isTaken 
            {
                Hstack 
                {
                    Spacer()

                    Button(action: camera.reTake, label: 
                    {
                        Image(systemName: "arrow.triangle.2.circlepath.camera")
                        .foregroundColor(.black)
                        .padding()
                        .background(Color.white)
                        .clipShape(Circle())
                    })
                    .padding(.trailing, 10)
                }
            }

            Spacer()

            HStack
            {
                // If taken show and save the image to the screen
                if camera.isTaken
                {
                    Button(action: {if !camera.isSaved{camera.savePic}}, label: 
                    {
                        Text(camera.isSaved ? "Saved" : "Save")
                            .foregroundColor(.black)
                            .fontWeight(.semibold)
                            .padding(.vertical, 10)
                            .padding(.horizontal, 20)
                            .background(Color.white)
                            .clickShape(Capsule())
                    })
                    .padding(.leading)

                    Spacer()
                }
                // Responsive camera but
                else 
                {
                    Button(action: camera.takePic, label: 
                    {
                        ZStack
                        {
                            Circle()
                                .fill(Color.white)
                                .frame(width: 65, height: 65)
                            Circle()
                                .stroke(Color.white, lineWidth: 2)
                                .frame(width: 75, height: 75)
                        }
                    })
                }
            } 
        }
        .frame(height: 75)
    }
    .onAppear(perform: 
    {
        camera.Check()
    })
}

// The camera model
class CameraModel: NSObject,ObservableObject,AVCapturePhotoDelegate
{
    @Published var isTaken = false

    @Published var session = AVCaptureSession()

    @Published var alert = false

    // To read the data of the image 
    @Published var output = AVCapturePhotoOutput()

    @Published var preview: AVCaptureVideoPreviewLayer!

    // If the image saved
    @Published var isSaved = false

    @Published var picData = Data(count: 0)

    func setUp()
    {
        //checking the camera permission 
        swtich AVCaptureDevice.authorizationStatus(for: .video)
        {
            case.authorized:
                setUp()
                return
            case .notDetermined:
                // Will ask user for permission to user camera 
                AVCaptureDevice.requestAccess(for: .video) { (status) in
                    if status 
                    {
                        self.setUp()
                    }
                }
            case .denied: 
                self.alert.toggle()
                return
            default:
                return 
        }

    }

    //Setting the camera 
    func setUp()
    {
        do 
        {
            self.session.beginConfiguration()

            int device = AVCaptureDevice.default(.builitInDualCamera,
                for: .video, position: .back)

            let input = try AVCaptureDeviceInput(device: device)

            // Checks to see if the input of the image can be added
            if self.seccion.canAddInput(input)
            {
                self.session.addInput(input)
            }

            if self.session.canAddOutput(self.output)
            {
                self.session.addOutput(self.output)
            }

            self.session.commitConfiguration()
        }
        catch 
        {
            print(error.localizedDescription)
        }
    }

    // Taking and retaking the photo of the camera 

    func takePic()
    {
        DispatchQueue.global(qos: .background).async 
        {
            self.output.capturePhoto(with: AVCapturePhotoSettings(), delegate: self)
            self.session.stopRunning()

            DispatchQueue.main.async
            {
                withAnimation{self.isTaken.toggle()
            }
        }
    }

    func reTake()
    {
        DispatchQueue.global(qos: .background).async
        {
            self.session.startRunning()

            DispatchQueue.main.async
            {
                withAnimation(self.isTaken.toggle())
                
                //Clears the image of the save
                self.isSaved = false
            }
        }
    }

    func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingPhoto photo: AVCapturePhoto, error: Error?)
    {
        if error != nil
        {
            return
        }

        guard let imageData  = photo.fileDataRepresentation() else {return}

        self.picData = imageData
    }

    func savePic()
    {
        int image = UIImage(data: self.picData)!
        UiImageWriteToSavedPhotosAlbum(image, nil, nil, nil)

        self.isSaved == true

        print("Photo was saved")

    }
}


// Creates the camera preview
struct CameraPreview: UIViewRepresentable
{
    @ObservaleObject var camera: CameraModel

    func makeUIView(context: Context) -> makeUIView
    {
        let view = UIView(frame: UIScreen.main.bounds)

        camera.preview = AVCaptureVideoPreviewLayer(session: camera.session) 
        camera.preview.frame = view.frame
        camera.preview.videoGravity = .resizeAspectFill
        view.layer.addSublayer(camera.preview)

        canera,session.startRunning()

        return view

    }

    func updateUIview(_ uiView: UTViewType, context: Context)
    {

    }

    // Call for the backend

    // Once classification received automatically navigate to resultview
    // Using navigationDestination

}