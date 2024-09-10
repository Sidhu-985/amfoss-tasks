import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'HeroPageDetails.dart';

class HeroesTab extends StatefulWidget {
  final List<Map<String, dynamic>> bookmarkedHeroes;

  const HeroesTab({super.key, required this.bookmarkedHeroes});

  @override
  State<HeroesTab> createState() => _HeroesTabState();
}

class _HeroesTabState extends State<HeroesTab> {

  void bookmark(Map<String,dynamic> hero){
    setState(() {
      if(widget.bookmarkedHeroes.contains(hero)){
        widget.bookmarkedHeroes.remove(hero);
      }
      else{
        widget.bookmarkedHeroes.add(hero);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          children: [
            if (widget.bookmarkedHeroes.isEmpty)
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
                  itemCount: widget.bookmarkedHeroes.length,
                  itemBuilder: (ctx, index) {
                    final hero = widget.bookmarkedHeroes[index];
                    return GestureDetector(
                      onTap: (){
                        Navigator.of(context).push(
                            MaterialPageRoute(builder: (ctx){
                          return HeroPageDetails(
                              hero: hero, isBookmarked: widget.bookmarkedHeroes.contains(hero), onBookmarkToggled: (){
                                bookmark(hero);
                          });
                        }));
                      },
                      child: ListTile(
                        title: Text(
                          hero['name'],
                          style:  GoogleFonts.alexandria(color: Colors.white),
                        ),
                        leading: Image.network(hero['images']['sm']),
                        trailing: const Icon(Icons.bookmark,
                          color: Colors.white,),
                      ),
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
