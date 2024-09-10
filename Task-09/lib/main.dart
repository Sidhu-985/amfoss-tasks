import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart' as rootBundle;
import 'HeroPageDetails.dart';
import 'heroes_Tab.dart';
import 'package:google_fonts/google_fonts.dart';
import 'account_Page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Hero Dex',
      theme: ThemeData(
        primaryColor: Colors.blue,
        indicatorColor: Colors.indigo,
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<dynamic> heroes = [];
  List<dynamic> searchHeroes = [];
  List<Map<String, dynamic>> bookmarkedHeroes = [];
  int current_index = 0;
  final _textcontroller = TextEditingController();
  final List<String> categories = ['Heroes', 'Villains', 'Anti-heroes'];
  List<String> selectedCategories = [];
  bool isfiltered = false;

  @override
  void initState() {
    super.initState();
    loadJsonData();
  }

  Future<void> loadJsonData() async {
    final String response = await rootBundle.rootBundle.loadString('assets/superhero.json');
    final data = await json.decode(response);
    setState(() {
      heroes = data;
      searchHeroes = data;
    });
  }

  void searchingHeroes(String query) {
    final filtered = heroes.where((hero) {
      final heroName = hero['name'].toString().toLowerCase();
      final input = query.toLowerCase();
      return heroName.contains(input);
    }).toList();

    setState(() {
      searchHeroes = filtered;
    });
  }

 void bookmark(Map<String,dynamic> hero){
    if(bookmarkedHeroes.contains(hero)){
      bookmarkedHeroes.remove(hero);
    }
    else{
      bookmarkedHeroes.add(hero);
    }
 }

  void filtercategory(){
    if(selectedCategories.isEmpty){
      setState(() {
        searchHeroes = heroes;
      });
      return;
    }

    final filtercategories = heroes.where((hero) {
      final hero_Alignment = hero['biography']['alignment'].toString().toLowerCase();
      return selectedCategories.any((category) {
        String categoryval = category.toLowerCase();

        if (categoryval == 'anti-heroes'){
          categoryval = 'neutral';
        }
        if (categoryval == 'villains'){
          categoryval = 'bad';
        }
        if (categoryval == 'heroes'){
          categoryval = 'good';
        }
        return hero_Alignment.contains(categoryval);
      });
    }).toList();

    setState(() {
      searchHeroes = filtercategories;
    });
  }

  @override
  Widget build(BuildContext context) {
    final pages = [
      homePageContent(),
      HeroesTab(bookmarkedHeroes: bookmarkedHeroes),
      const AccountPage()
    ];

    return Scaffold(
      backgroundColor: Colors.black87,
      appBar: AppBar(
        backgroundColor: Colors.black,
        title: Center(
          child: Text(
            "HERO-DEX",
            style: GoogleFonts.mingzat(
              fontSize: 25,
              fontWeight: FontWeight.w800,
              color: Colors.white,
            ),
          ),
        ),
      ),
      body: pages[current_index],
      bottomNavigationBar: BottomNavigationBar(
        selectedItemColor: Colors.white,
        unselectedItemColor: Colors.grey,
        backgroundColor: Colors.black,
        currentIndex: current_index,
        onTap: (newIndex) {
          setState(() {
            current_index = newIndex;
          });
        },
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
          BottomNavigationBarItem(icon: Icon(Icons.bookmark), label: "Heroes Tab"),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: "Account"),
        ],
      ),
    );
  }

  Widget homePageContent() {
    return Padding(
      padding: const EdgeInsets.all(17),
      child: Column(
        children: [
          Container(
            decoration: BoxDecoration(
              color: Colors.greenAccent,
              borderRadius: BorderRadius.circular(20),
            ),
            child: TextField(
              controller: _textcontroller,
              decoration: InputDecoration(
                hintText: 'Search for a hero...',
                prefixIcon: const Icon(Icons.search),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(20),
                  borderSide: BorderSide.none,
                ),
              ),
              onChanged: (value) {
                if (value.isEmpty) {
                  const AlertDialog(title: Text("No input is entered"));
                } else {
                  searchingHeroes(value);
                }
              },
            ),
          ),
          const SizedBox(height: 10),
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: categories.map((category) {
                return Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 5),
                  child: FilterChip(
                    selected: selectedCategories.contains(category),
                    label: Text(
                      category,
                      style: TextStyle(
                        color: selectedCategories.contains(category) ? Colors.black : Colors.black,
                      ),
                    ),
                    onSelected: (bool selected) {
                      setState(() {
                        if (selected) {
                          selectedCategories.add(category);
                        } else {
                          selectedCategories.remove(category);
                        }
                        filtercategory();
                      });
                    },
                    backgroundColor: Colors.grey.shade300,
                    selectedColor: Colors.lightGreenAccent,
                  ),
                );
              }).toList(),
            ),
          ),
          const SizedBox(height: 30),
          Expanded(
            child: Container(
              color: Colors.black12,
              child: GridView.builder(
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 2,
                  childAspectRatio: 0.64,
                  crossAxisSpacing: 15,
                  mainAxisSpacing: 15,
                ),
                itemCount: searchHeroes.length,
                itemBuilder: (ctx, index) {
                  final hero = searchHeroes[index];
                  return GestureDetector(
                    onTap: () {
                      Navigator.of(context).push(MaterialPageRoute(
                        builder: (ctx) {
                          return HeroPageDetails(
                            hero: hero,
                            isBookmarked: bookmarkedHeroes.contains(hero),
                            onBookmarkToggled: () {
                              bookmark(hero);
                            },
                          );
                        },
                      ));
                    },
                    child: Container(
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Column(
                        children: [
                          ClipRRect(
                            borderRadius: const BorderRadius.only(
                              topLeft: Radius.circular(10),
                              topRight: Radius.circular(10),
                            ),
                            child: Image.network(
                              hero['images']['lg'],
                              fit: BoxFit.cover,
                              width: 200,
                              height: 200,
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(8),
                            child: Text(
                              hero['name'],
                              style: GoogleFonts.alata(
                                color: Colors.black,
                                fontSize: 20,
                                fontWeight: FontWeight.bold,
                              ),
                              textAlign: TextAlign.center,
                            ),
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
            ),
          ),
        ],
      ),
    );
  }
}
