class Timer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            seconds: 0,
            running: false
        };
        this.tick = this.tick.bind(this);
    }
    
    tick() {
        this.setState(
            {
                seconds: this.state.seconds + 1,
                running: yes,
            }
        );
    }
    
    componentDidMount() {
        this.interval = setInterval(() => this.tick(), 1000);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }
    

    render() {
        const radius = 300;
        const timerStyle = {
            width: radius,
            height: radius,
            borderRadius: radius/2,
            margin: 'auto',
            textAlign: 'center',
            fontSize: 72,
            fontFamily: 'sans-serif',
            backgroundColor: "#FFC53A",
        };
    
        return (
            <div style = {timerStyle}>
                {this.state.seconds}
            </div>
        );
    }
}

class Button extends React.Component {
    constructor(props) {
        super(props);
        this.state({buttonText: "Start" });
    }

    updateButtonText() {

    }

    render() {
        const buttonStyle = {
            color: '#F00',
            fontSize: 24,
            fontFamily: 'sans-serif',
            textAlign: 'center',
            fontWeight: 'bold'
        };

        return (
            <div style = {buttonStyle}>
                {this.state.buttonText}
            </div>
        );
    }
}

ReactDOM.render (
    <div>
        <Timer />
        <Button />
    </div>,
    document.getElementById('container')
);