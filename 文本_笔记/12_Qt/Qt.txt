// 取消窗口边框
setWindowFlags(Qt::FramelessWindowHint);

// 设置大小位置
this -> setGeometry(Window_x, Window_y, Window_width, Window_height);

//如果隐藏边框后还想要把该界面至于其他界面的顶层，可以使用以下代码：
this->setWindowFlags(Qt::X11BypassWindowManagerHint | Qt::WindowStaysOnTopHint |Qt::FramelessWindowHint);

5.QMouseEvent* e;
  e->globalPos();
Returns the global position of the mouse cursor at the time of the event.
返回事件发生时鼠标光标的全局位置。

// 隐藏任务栏中的图标：
this->setWindowFlags(Qt::Tool);

// 绘图事件
{
// 线
QPainter.drawLine(QPoint( , ), QPoint( , ));
//椭圆 圆
QPainter.drawellilpse(QPoint( , ), 50, 50);
// 矩形
QPainter.draweRect(QRect(QRect( , , , )));
// 文字
QPainter.drawText(QRect( , , , ), "asdasd");

}

// 水平  Qt::Horizontal
// 垂直  Qt::Vertical

```cpp
qRegisterMetaType<uint8_t>("uint8_t"); // 注册类型
```



















