import React, {Component} from 'react';
import EndQuestionaire from './EndQuestionaire.js'

class LoadQuestionaire extends Component {

    answers = [];
    state = {
        questionID: 0,
        questionaireID: 0,
        question: null,
        option1: null,
        option2: null,
        option3: null,
        option4: null,
        answer: null,
        score: 0,
        endQuiz: 0,
        totalQuestions : 0
    }

    loadQuestion(questionaireId, questionId) {
        fetch('http://127.0.0.1:8000/api/v1/',
            {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    questionaireID: questionaireId,
                    QuestionID: questionId
                })
            })
            .then(response => {
                if (response.status == 200)
                {
                    this.setState({totalQuestions: this.state.totalQuestions + 1});
                    return response.json();
                }
                else if (response.status == 500)
                {
                    this.setState({endQuiz: 1})
                    return  response.json();
                }
            })
            .then(
                data => {

                    this.setState(() => {
                        return {
                            questionID: questionId,
                            questionaireID: questionaireId,
                            question: data.question,
                            option1: data.option1,
                            option2: data.option2,
                            option3: data.option3,
                            option4: data.option4,
                            answer: data.answer
                        }
                    });
                    if (this.state.questionID==1){
                        this.answers.push(this.state.question)
                    }

                })
            .catch(error => console.error(error))
    }

    loadNextQuestion=(answer)=> {

         if (this.state.answer == answer){
             this.setState({score: this.state.score + 1});
         }
        this.answers.push(answer)
        this.setState({questionID: this.state.questionID})
        this.loadQuestion(this.state.questionaireID, this.state.questionID+1)
    }


    async componentDidMount() {
        this.loadQuestion(this.props.questionaireID, 1)

    }

    render() {
        if (this.state.endQuiz ==1)
        {
            return (
                <div>
                    <EndQuestionaire score = {this.state.score} total = {this.state.totalQuestions} answers = {this.answers}/>

                </div>
            )
        }
        return(
            <div>
                <h5>  {this.state.question} </h5>
                <button onClick={ () => this.loadNextQuestion(this.state.option1)} > {this.state.option1}</button><br/>
                <button onClick={() => this.loadNextQuestion(this.state.option2)} > {this.state.option2}</button><br/>
                <button onClick={() => this.loadNextQuestion(this.state.option3)} > {this.state.option3}</button><br/>
                <button onClick={() => this.loadNextQuestion(this.state.option4)} > {this.state.option4}</button><br/>

            </div>

        );
    }
}



export default LoadQuestionaire