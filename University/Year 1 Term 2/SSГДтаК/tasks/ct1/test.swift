import UIKit
import PlaygroundSupport

let view = UIView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
view.backgroundColor = .red

let label = UILabel(frame: CGRect(x: 50, y: 50, width: 100, height: 50))
label.text = "Hello, Playgrounds!"
label.textColor = .white
label.textAlignment = .center

view.addSubview(label)

PlaygroundPage.current.liveView = view