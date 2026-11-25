Windows: Python 3.13.1

Sur chaque machine, il suffira de faire :

bash
python -m venv .venv
# activation : source .venv/bin/activate (Mac/Linux) ou .venv\Scripts\activate (Windows)
pip install -r requirements.txt




import 'package:flutter/material.dart';

void main() {
  runApp(const ButtonApp());
}

class ButtonApp extends StatelessWidget {
  const ButtonApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(home: MyButton());
  }
}

class MyButton extends StatelessWidget {
  const MyButton({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Button ex00')),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Press the button below!'),
            const SizedBox(height: 20),
            FloatingActionButton(
              onPressed: () {
                debugPrint('Button pressed');
              },
              child: const Icon(Icons.add),
            ),
          ],
        ),
      ),
    );
  }
}
