//
//  Tab.swift
//  FoodDeliveryApp
//
//  Created by Balaji on 08/09/22.
//

import SwiftUI

// MARK: Tab Model And Sample Data
struct Tab: Identifiable{
    var id: String = UUID().uuidString
    var tabImage: String
    var tabName: String
    var tabOffset: CGSize
}

var tabs: [Tab] = [
    .init(tabImage: "Shake 2",tabName: "Hot\nCoffee", tabOffset: CGSize(width: 0, height: -40)),
    .init(tabImage: "Shake 1",tabName: "Frappo", tabOffset: CGSize(width: 0, height: -38)),
    .init(tabImage: "Shake 3",tabName: "Ice Cream", tabOffset: CGSize(width: 0, height: -25)),
    .init(tabImage: "Shake 4",tabName: "Waffles", tabOffset: CGSize(width: -12, height: 28))
]
