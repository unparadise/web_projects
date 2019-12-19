class Counter extends React.Component {
    render() {
        const textStyle = {
            fontSize: 72,
            fontFamily: "sans-serif",
            color: "#333",
            fontWeight: "bold"
        };

        return(
            <div style={textStyle}>
                {this.props.display}
            </div>
        );
    };
}

class CounterParent extends React.Component {
    constructor(props) { // In ES6, constructor is how default states are decleared
        super(props);
        this.state = {count: 0};
        this.increase = this.increase.bind(this); // In ES6, manual bind is required
    }

    increase(e) {
        if(e.shiftKey) {
            this.setState({count: this.state.count + 10});
        } else {
            this.setState({count: this.state.count + 1});
        }
        
    }

    render() {
        const backgroundStyle = {
            padding: 50,
            backgroundColor: "#FFC53A",
            width: 250,
            height: 100,
            borderRadius: 10,
            textAlign: "center"
        };

        return(
            <div style={backgroundStyle}>
                <Counter display={this.state.count} />
                <PlusButton clickHandler={this.increase}></PlusButton>
            </div>
        );
    }
}

class PlusButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = {buttonText: "Add 1"};
        this.updateButtonText = this.updateButtonText.bind(this);
    }

    updateButtonText(e) {
        if(e.shiftKey) {
            this.setState({buttonText: "Add 10"});
        } else {
            this.setState({buttonText: "Add 1"});
        }
    }

    componentDidMount() {
        document.addEventListener('keydown', this.updateButtonText);
        document.addEventListener('keyup', this.updateButtonText);
    }

    componentWillUnmount() {
        document.removeEventListener('keydown', this.updateButtonText);
        document.addEventListener('keyup', this.updateButtonText);
    }

    render() {
        const buttonStyle = {
            fontSize: "1em",
            paddingTop: 4,
            marginTop: 12,
            width: 120,
            height: 30,
            fontFamily: "sans-serif",
            color: "#333",
            borderRadius: 15,
            fontWeight: "bold",
            lineHeight: "3px"
        };

        return (
            <button onClick = {this.props.clickHandler} style={buttonStyle}>
            {this.state.buttonText}
            </button>
        );
    }
}

ReactDOM.render (
    <div>
        <CounterParent />
    </div>,
    document.getElementById("container")
);