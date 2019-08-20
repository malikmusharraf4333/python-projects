import React, {Component} from 'react';
import LoadQuestionaire from './Components/LoadQuestionaire.js'
class fQuestionaire extends Component{

    questionID = 1;
constructor(props){
    super(props)
this.selectedQuestionaire = this.selectedQuestionaire.bind(this);
}


    state = {
        questionaires: [],
        question : null,
        option1: null,
        option2: null,
        option3: null,
        option4: null,
        answer: null,
        renderView:0

    }


    loadQuestions = () =>
    {
        fetch ( 'http://127.0.0.1:8000/api/questionaire//',
            {
                    method: 'GET',
                    headers: {'Content-Type': 'application/json'},

                 })
        .then (data => data.json())
            .then (
                data => {
                    this.setState ({questionaires: data});
    })
        .catch (error => console.error(error))


     };



componentDidMount() {
    this.loadQuestions()
}


selectedQuestionaire(id)
{
    if (id)
    {
        this.setState({renderView : id})
    }

}



render() {
    if (this.state.renderView)
    {
        return ( <div>
            <LoadQuestionaire questionaireID = {this.state.renderView}/>
        </div>)

    }

    return(
        <div>
            <h1>
                Select one of the following Questionaire
            </h1>

        {   this.state.questionaires.map ( question => {
               return <button className='bg-primary' onClick={this.selectedQuestionaire.bind(this, question.id)} key={question.id}>  {question.name}  </button>}
        )}

    </div>


)
}
}



export default fQuestionaire;
