import 'dart:convert';
import 'package:http/http.dart' as http;
class ApiClient {
  final String baseUrl = 'http://10.0.2.2:8000';
  Future<List<dynamic>> getWorkouts(int userId) async {
    final res = await http.get(Uri.parse('$baseUrl/workouts/user/$userId'));
    if (res.statusCode != 200) throw Exception('Failed');
    return jsonDecode(res.body) as List<dynamic>;
  }
  Future<void> createWorkout(Map<String, dynamic> payload) async {
    final res = await http.post(
      Uri.parse('$baseUrl/workouts/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode(payload),
    );
    if (res.statusCode >= 300) throw Exception('Failed');
  }
}