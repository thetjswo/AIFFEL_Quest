import 'package:flutter/material.dart';
import 'package:flutter_native_splash/flutter_native_splash.dart';
import 'real_time_video.dart';

void main() {
  WidgetsBinding widgetsBinding = WidgetsFlutterBinding.ensureInitialized();
  FlutterNativeSplash.preserve(widgetsBinding: widgetsBinding);

  runApp(MyApp());

  FlutterNativeSplash.remove();
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'test',
      theme: ThemeData(primarySwatch: Colors.cyan),
      home: MainPage(),
    );
  }
}

class MainPage extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color(0xFFF5EFFB),
        title: Text(
          'BodyGuard',
          style: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.bold,
            fontStyle: FontStyle.italic,
          ),
        ),
        centerTitle: true,
        elevation: 1,
        bottom: PreferredSize(
          preferredSize: Size.fromHeight(1.0),
          child: Container(
            color: Color(0xFFD0A9F5),
            height: 1.0,
          ),
        ),
      ),
      drawer: Drawer(
        child: ListView(
          children: [
            ListTile(
              title: Text('실시간 영상 확인'),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => RealTimePage()),
                );
              },
            ),
            ListTile(
              title: Text('위험 알림 영상 확인'),
              onTap: () {
                // 메뉴 항목 2를 선택했을 때 할 일 추가
              },
            ),
            ListTile(
              title: Text('항목을 입력하세요.'),
              onTap: () {
                // 메뉴 항목 2를 선택했을 때 할 일 추가
              },
            )
          ],
        ),
      ),
      body: Container(
        margin: EdgeInsets.all(20),
        child: Column(
          children: [
            Container(
              margin: EdgeInsets.only(top: 30),
              child: Column(
                children: [
                  Text(
                    'Dash Board',
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  SizedBox(height: 70),
                  Align(
                    alignment: Alignment.centerLeft,
                    child: Text(
                      '<주간 알림 현황>',
                      textAlign: TextAlign.left,
                    ),
                  ),
                  //TODO: backend에서 집계된 데이터를 불러와서 그래프 그리기
                  Image.asset('images/dashboard_graph.png'),
                  SizedBox(height: 30),
                  Align(
                    alignment: Alignment.centerLeft,
                    child: Text(
                      '<위험도 알림 현황>',
                      textAlign: TextAlign.left,
                    ),
                  ),
                  //TODO: backend에서 집계된 데이터를 불러와서 그래프 그리기
                  Image.asset('images/dashboard_bar_graph.png'),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}