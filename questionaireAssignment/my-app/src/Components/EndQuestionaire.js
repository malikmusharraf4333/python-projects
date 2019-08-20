import React, {Component} from 'react';

class EndQuestionaire extends Component {

    state = {
        score:0,
        TotalQuestion:0,
        answers:[]
    }
    componentDidMount() {
        this.setState({score:this.props.score , TotalQuestion: this.props.total , answers: this.props.answers})
        this.props.answers.map(answer => {
            console.log(answer)
        })


    }

    render() {
        return(
            <div>
                <h1>
                    You Scored: {this.state.score}
                </h1>
                <h1>
                    Total Questions: {this.state.TotalQuestion}
                </h1>
            </div>
        )
    }
}

export default EndQuestionaire