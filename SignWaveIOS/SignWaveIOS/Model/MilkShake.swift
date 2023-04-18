//
//  MilkShake.swift
//  FoodDeliveryApp
//
//  Created by Balaji on 08/09/22.
//

import SwiftUI

// MARK: Model And Sample Data
struct MilkShake: Identifiable,Hashable{
    var id: String = UUID().uuidString
    var title: String
    var price: String
    var image: String
}

var milkShakes: [MilkShake] = [
    .init(title: "Promise", price: "Definitely do something or give them something.", image: "Shake 1"),
    .init(title: "Clapping", price: "A clap is the percussive sound made by striking together two flat surfaces", image: "Shake 2"),
    .init(title: "Okay", price: "Denoting approval, acceptance, agreement, assent, acknowledgment, or a sign of indifference.", image: "Shake 3"),
    .init(title: "Washing Hands", price: "can keep you healthy and prevent the spread of respiratory and diarrheal infections.", image: "Shake 4"),
]
