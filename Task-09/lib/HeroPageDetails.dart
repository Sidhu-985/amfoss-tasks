import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'fonts/MyFlutterApp.ttf/my_flutter_app_icons.dart';

class HeroPageDetails extends StatefulWidget {
  final Map<String, dynamic> hero;
  final bool isBookmarked;
  final VoidCallback onBookmarkToggled;

  const HeroPageDetails({
    super.key,
    required this.hero,
    required this.isBookmarked,
    required this.onBookmarkToggled,
  });

  @override
  _HeroPageDetailsState createState() => _HeroPageDetailsState();
}

class _HeroPageDetailsState extends State<HeroPageDetails> {
  late bool _isBookmarked;

  @override
  void initState() {
    super.initState();
    _isBookmarked = widget.isBookmarked;
  }

  @override
  Widget build(BuildContext context) {
    if (widget.hero['appearance']['race'] == null) {
      setState(() {
        widget.hero['appearance']['race'] = "Unknown";
      });
    }
    return Scaffold(
      backgroundColor: Colors.black12,
      body: SafeArea(
        child: Column(
          children: [
            Row(
              children: [
                IconButton(
                  onPressed: () {
                    Navigator.of(context).pop();
                  },
                  icon: const Icon(Icons.arrow_back, color: Colors.white),
                ),
                Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: Text(
                    widget.hero['name'],
                    style:  GoogleFonts.abel(
                      color: Colors.white,
                      fontSize: 20,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ),
                const Spacer(),
                IconButton(
                  onPressed: () {
                    setState(() {
                      _isBookmarked = !_isBookmarked;
                    });
                    widget.onBookmarkToggled();
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        duration: const Duration(seconds: 2),
                        content: Text(
                          _isBookmarked
                              ? "Added to Heroes Tab"
                              : "Removed from Heroes Tab",
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 17,
                          ),
                        ),
                      ),
                    );
                  },
                  icon: Icon(
                    _isBookmarked
                        ? Icons.bookmark
                        : Icons.bookmark_outline_outlined,
                    size: 30,
                    color: Colors.white,
                  ),
                ),
              ],
            ),
            Expanded(
              child: SingleChildScrollView(
                child: Column(
                  children: [
                    Center(
                      child: SizedBox(
                        height: 400,
                        width: 250,
                        child: Image.network(
                          widget.hero['images']['lg'],
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.all(20),
                      child: Text(
                        "Power Stats",
                        style: GoogleFonts.sail(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                          fontSize: 30,
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 20.0),
                      child: Column(
                        children: [
                          PowerStatRow(
                            icon: Icons.psychology,
                            label: "Intelligence",
                            value: widget.hero['powerstats']['intelligence'],
                          ),
                          PowerStatRow(
                            icon: Icons.fitness_center,
                            label: "Strength",
                            value: widget.hero['powerstats']['strength'],
                          ),
                          PowerStatRow(
                            icon: Icons.bolt,
                            label: "Speed",
                            value: widget.hero['powerstats']['speed'],
                          ),
                          PowerStatRow(
                            icon: Icons.shield,
                            label: "Durability",
                            value: widget.hero['powerstats']['durability'],
                          ),
                          PowerStatRow(
                            icon: Icons.flash_on,
                            label: "Power",
                            value: widget.hero['powerstats']['power'],
                          ),
                          PowerStatRow(
                            icon: MyFlutterApp.crossed_swords,
                            label: "Combat",
                            value: widget.hero['powerstats']['combat'],
                          ),
                        ],
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.all(20),
                      child: Text(
                        "Appearance",
                        style: GoogleFonts.sail(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                          fontSize: 30,
                          fontStyle: FontStyle.italic,
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 20.0),
                      child: Column(
                        children: [
                          Appearance(
                            label: "Gender:",
                            val: widget.hero['appearance']['gender'],
                          ),
                          Appearance(
                            label: "Race:",
                            val: widget.hero['appearance']['race'],
                          ),
                          Appearance(
                            label: "Height:",
                            val: widget.hero['appearance']['height'][0],
                          ),
                          Appearance(
                            label: "Weight:",
                            val: widget.hero['appearance']['weight'][1],
                          ),
                          Appearance(
                            label: "Eye Color:",
                            val: widget.hero['appearance']['eyeColor'],
                          ),
                          Appearance(
                            label: "Hair Color:",
                            val: widget.hero['appearance']['hairColor'],
                          ),
                        ],
                      ),
                    ),
                     Padding(
                      padding:const EdgeInsets.all(20),
                      child: Text(
                        "Biography",
                        style: GoogleFonts.sail(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                          fontSize: 30,
                          fontStyle: FontStyle.italic,
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 20.0),
                      child: Column(
                        children: [
                          Biography(
                            label: "Full Name:",
                            val: widget.hero['biography']['fullName'],
                          ),
                          Biography(
                            label: "Alter Egos:",
                            val: widget.hero['biography']['alterEgos'],
                          ),
                          Biography(
                            label: "Aliases:",
                            val: widget.hero['biography']['aliases'][0],
                          ),
                          Biography(
                            label: "Place of Birth:",
                            val: widget.hero['biography']['placeOfBirth'],
                          ),
                          Biography(
                            label: "First Appearance:",
                            val: widget.hero['biography']['firstAppearance'],
                          ),
                          Biography(
                            label: "Publisher:",
                            val: widget.hero['biography']['publisher'],
                          ),
                          Biography(
                            label: "Alignment:",
                            val: widget.hero['biography']['alignment'],
                          ),
                        ],
                      ),
                    ),
                     Padding(
                      padding:const EdgeInsets.all(20),
                      child: Text(
                        "Work",
                        style: GoogleFonts.sail(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                          fontSize: 30,
                          fontStyle: FontStyle.italic,
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 20),
                      child: Column(
                        children: [
                          Work(
                              label: "Occupation:",
                              val: widget.hero['work']['occupation']),
                          Work(label: "Base:", val: widget.hero['work']['base']),
                        ],
                      ),
                    ),
                     Padding(
                      padding:const EdgeInsets.all(20),
                      child: Text(
                        "Connections",
                        style: GoogleFonts.sail(
                            color: Colors.white,
                            fontSize: 30,
                            fontWeight: FontWeight.bold,
                            fontStyle: FontStyle.italic),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 20),
                      child: Column(
                        children: [
                          Connections(
                            label: "Group Affiliation:",
                            val: widget.hero['connections']['groupAffiliation'],
                          ),
                          Connections(
                              label: "Relative:",
                              val: widget.hero['connections']['relatives'])
                        ],
                      ),
                    )
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
class PowerStatRow extends StatelessWidget {
  final IconData icon;
  final String label;
  final int value;

  const PowerStatRow(
      {super.key, required this.icon, required this.label, required this.value});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: [
              Icon(
                icon,
                color: Colors.white,
                size: 30,
              ),
              const SizedBox(width: 10),
              Text(
                label,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 18,
                ),
              ),
            ],
          ),
          Text(
            value.toString(),
            style: const TextStyle(
              color: Colors.white,
              fontSize: 18,
            ),
          ),
        ],
      ),
    );
  }
}

class Appearance extends StatelessWidget {
  final String label;
  final String val;

  const Appearance({super.key, required this.label, required this.val});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Row(
        children: [
          Expanded(
            child: Text(
              label,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 18,
              ),
            ),
          ),
          Expanded(
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Text(
                val,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 18,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class Biography extends StatelessWidget {
  final String label;
  final String val;

  const Biography({super.key, required this.label, required this.val});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: Text(
              label,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 18,
              ),
            ),
          ),
          Expanded(
            child: Text(
              val,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 18,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class Work extends StatelessWidget {
  final String label;
  final String val;

  const Work({super.key, required this.label, required this.val});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: Text(
              label,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 18,
              ),
            ),
          ),
          Expanded(
            child: Text(
              val,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 18,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class Connections extends StatelessWidget {
  final String label;
  final String val;

  const Connections({super.key, required this.label, required this.val});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: Text(
              label,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 18,
              ),
            ),
          ),
          Expanded(
            child: Text(
              val,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 18,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
