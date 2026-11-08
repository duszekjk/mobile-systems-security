//
//  ContentView.swift
//  LessonH_iOSBank
//
//  Created by Jacek Kałużny on 6/16/26.
//

import SwiftUI

struct ContentView: View {
    @State private var accountName = "Lesson H Checking"
    @State private var amount = "42.50"
    @State private var memo = "Test payment"
    @State private var status = "Mock bank ready"

    var body: some View {
        NavigationStack {
            Form {
                Section("Transfer") {
                    TextField("Account", text: $accountName)
                    TextField("Amount", text: $amount)
                    TextField("Memo", text: $memo)
                }

                Section("Actions") {
                    Button("Send payment") {
                        status = "Queued \(amount) to \(accountName)"
                    }
                    Button("Refresh ledger") {
                        status = "Connected to local fake server"
                    }
                }

                Section("Status") {
                    Text(status)
                }
            }
            .navigationTitle("Lesson H Bank")
        }
    }
}

#Preview {
    ContentView()
}
