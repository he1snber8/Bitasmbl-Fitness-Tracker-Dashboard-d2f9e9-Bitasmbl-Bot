import 'package:flutter/material.dart';
import 'services/api_client.dart';
void main() => runApp(const FitnessApp());
class FitnessApp extends StatelessWidget {
  const FitnessApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Fitness Tracker',
      home: const DashboardScreen(),
    );
  }
}
class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});
  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}
class _DashboardScreenState extends State<DashboardScreen> {
  List workouts = [];
  @override
  void initState() {
    super.initState();
    _load();
  }
  Future<void> _load() async {
    final data = await ApiClient().getWorkouts(1);
    setState(() => workouts = data);
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Fitness Dashboard')),
      body: ListView(
        children: workouts
            .map<Widget>((w) => ListTile(
                  title: Text('${w['type']} - ${w['duration_min']} min'),
                  subtitle: Text('${w['calories']} kcal'),
                ))
            .toList(),
      ),
    );
  }
}