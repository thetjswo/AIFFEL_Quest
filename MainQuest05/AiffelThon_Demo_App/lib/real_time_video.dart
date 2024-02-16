import 'package:flutter/material.dart';
// import 'package:video_player/video_player.dart';
// // import 'package:flutter_fastapi/flutter_fastapi.dart';
// import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:web_socket_channel/io.dart';
import 'main.dart';

class RealTimePage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return RealTimeState();
  }
}

class RealTimeState extends State<RealTimePage> {
  // VideoPlayerController _videoPlayerController;
  // WebSocketChannel _cahnnel;
  // List<ObjectDetectionResult> _results = [];
  final channel = WebSocketChannel.connect(Uri.parse('ws://localhost:8000/stream'));

  // @override
  // void initState() {
  //   super.initState();
  //
  //   // 웹소켓 연결 및 데이터 수신
  //   WebSocketChannel _channel = WebSocketChannel.connect(
  //     url: 'ws://localhost:8000/stream',
  //     onMessage: (message) {
  //       if (message is String) {
  //         _results = _parseObjectDetectionResults(message);
  //         setState(() {}); // UI 업데이트
  //       }
  //     },
  //   );
  //
  //   // 비디오 플레이어 초기화
  //   VideoPlayerController _videoController = VideoPlayerController.network('ws://localhost:8000/stream');
  //   _videoController.initialize().then((_) {
  //     setState(() {});
  //   });
  // }

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
      body: Center(
        child: StreamBuilder(
          stream: channel.stream,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return Image.memory(
                snapshot.data,
                width: 640,
                height: 480,
                fit: BoxFit.cover,
              );
            } else if (snapshot.hasError) {
              return Text('Error: ${snapshot.error}');
            }
            return CircularProgressIndicator();
          },
        ),
      ),
    );
  }

  @override
  void dispose() {
    channel.sink.close();
    super.dispose();
  }
}
