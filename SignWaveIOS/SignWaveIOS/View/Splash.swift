//
//  Splash.swift
//  FoodDeliveryApp
//
//  Created by Shinjan Patra on 09/04/23.
//

import SwiftUI

struct Splash: View {
    @State private var isActive = false
    @State private var size = 0.8
    @State private var opacity = 0.5
    var body: some View {
        if isActive {
            ContentView()
        } else{
            VStack{
                VStack{
                    Image("logo")
                        .resizable()
                        .frame(width: 360, height: 450 )
                    Text("made by Binary Bosses with ❤️")
                        .fontWeight(.bold)
                        .foregroundColor(.red)
                    
                }
                .scaleEffect(size)
                .opacity(opacity)
                .onAppear{
                    withAnimation(.easeIn(duration: 1.5)){
                        self.size = 0.9
                        self.opacity = 1.0
                    }
                }
            }
            .onAppear{
                DispatchQueue.main.asyncAfter(deadline: .now() + 3.0){
                    self.isActive = true
                }
            }
        }
        
    }
}

struct Splash_Previews: PreviewProvider {
    static var previews: some View {
        Splash()
    }
}
