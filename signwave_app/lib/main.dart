import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:signwave_app/screens/home_page.dart';
import 'package:signwave_app/screens/camera.dart';

List<CameraDescription>? cameras;
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  cameras = await availableCameras();
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: MyHomePage(
    
    ),
  ));
}
