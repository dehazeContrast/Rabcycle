import SwiftUI

// Proceed back button
struct resultview: View {
    var body: some View {
        // Classification
        Text()
            .font(Font..custom("PixelifySans", size: 18))
            .padding(scaledPadding)
    }
}
var recylable: Bool
switch <classification> {
    case <plastic_waste>
    return true
    case <paper_and_cardboard>
    return true
    case <glass>
    return true
    case <metal>
    return true
    case <textile>
    return true
    case <organic_waste>1 
    return false
}
struct resultview_previews: PreviewProvider {
    static var previews: some View {
        resultview()
    }
}
// Displays image taken from camera.swift


// Display image then offset a box under it to the right
struct ZStack<Content> where Content : View {
    var body: some View {
        ZStack {
            if recyclable {
                
            }

            else {

            }


            @Image(source: camera_image, alt: String?) {
            }
            Rectangle()
                .fill(green)
                .frame(width: 318, height: 385)
                .offset(x: CGFloat($0) * 10.0)
        }
    }
}

// Grab classification from backend of program
// if classification was unable to to be returned, try again


// Switch statement using classification
// display classification as str and recyclabilility





// Display recyclability under classification
