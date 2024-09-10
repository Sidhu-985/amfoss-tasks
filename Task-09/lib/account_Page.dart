import 'dart:io';

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class AccountPage extends StatelessWidget {
  const AccountPage({super.key});

  @override
  Widget build(BuildContext context) {
    List<String> acc = ["Full Name:", "User name:", "Email:", "Phone number:", "ID:",""];
    List<String> details = ["John Doe","johndoe69","johndoe985@gmail.com","911XXXXXXXX","3642347DHM79E",""];

    return Scaffold(
      backgroundColor: Colors.black,
      body: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          children: [
            const Center(
              child: Icon(
                Icons.person_rounded,
                color: Colors.white,
                size: 200,
              ),
            ),
            Expanded(
              child: ListView.separated(
                itemCount: acc.length,
                itemBuilder: (ctx, index) {
                  return ListTile(
                    title: Text(
                      acc[index],
                      style: GoogleFonts.alexandria(
                        color: Colors.white,
                        fontSize: 20,
                      ),
                    ),
                    trailing: Text(
                        details[index],
                    style: const TextStyle(
                      color: Colors.white,
                     fontSize: 20
                    ),),
                  );
                },
                separatorBuilder: (ctx, index) {
                  return const Divider(color: Colors.grey);
                },
              ),
            ),
            ElevatedButton(onPressed: () => showDialog<String>(
              context: context,
              builder: (BuildContext context) => AlertDialog(
                title: const Text('Thank You'),
                actions: <Widget>[
                  TextButton(
                    onPressed: () => Navigator.pop(context, 'Cancel'),
                    child: const Text('Cancel'),
                  ),
                  TextButton(
                    onPressed: () => exit(0),
                    child: const Text('OK'),
                  ),
                ],
              ),
            ), child: const Text("Log Out",style: TextStyle(color: Colors.black,fontSize: 14),))
          ],
        ),
      ),
    );
  }
}