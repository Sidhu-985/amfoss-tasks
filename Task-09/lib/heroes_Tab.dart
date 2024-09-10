import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class HeroesTab extends StatelessWidget {
  final List<Map<String, dynamic>> bookmarkedHeroes;

  const HeroesTab({super.key, required this.bookmarkedHeroes});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          children: [
            if (bookmarkedHeroes.isEmpty)
              const Center(
                child: Text(
                  'No heroes are bookmarked',
                  style: TextStyle(
                      color: Colors.white,
                      fontSize: 20),
                ),
              )
            else
              Expanded(
                child: ListView.separated(
                  itemCount: bookmarkedHeroes.length,
                  itemBuilder: (ctx, index) {
                    final hero = bookmarkedHeroes[index];
                    return ListTile(
                      title: Text(
                        hero['name'],
                        style:  GoogleFonts.alexandria(color: Colors.white),
                      ),
                      leading: Image.network(hero['images']['sm']),
                      trailing: const Icon(Icons.bookmark,
                        color: Colors.white,),
                    );
                  },
                  separatorBuilder: (ctx,index){
                    return const SizedBox(
                      height: 50,
                        child: (Divider()));
                  },
                ),
              ),
          ],
        ),
      ),
    );
  }
}
