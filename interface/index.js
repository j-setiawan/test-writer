testTemplate = {};

function updateTemplate() {
    let text = document.getElementById('test-text-area');
    text.textContent = '';

    for (const question of Object.values(testTemplate)) {
        text.textContent += `${question['type']} ${question['points']}\n${question['question']}\n`;

        for (const choice of Object.values(question['choices'])) {
            text.textContent += `${choice}\n`;
        }

        text.textContent += '\n';
    }
}

function addQuestionToTemplate(id, type, question, points) {
    testTemplate[id] = {
        'type': type,
        'points': points,
        'question': question,
        'choices': {}
    };

    updateTemplate();
}

function addChoiceToQuestion(id, choiceId, choice) {
    testTemplate[id]['choices'][choiceId] = choice;
    updateTemplate();
}

function removeChoiceFromQuestion(id, choiceId) {
    testTemplate[id]['choices'].remove(choiceId);
    updateTemplate();
}

function createElement(elTag, elClass='', elId='', elText='', elAttr={}) {
    let el = document.createElement(elTag);
    el.className = elClass;
    el.id = elId;

    if (elText) {
        el.appendChild(document.createTextNode(elText));
    }

    for (const [key, value] of Object.entries(elAttr)) {
        el.setAttribute(key, value);
    }

    return el;
}

function createDiv(divClass, divId='') {
    return createElement('div', divClass, divId);
}

function createRow() {
    return createDiv('row');
}

function createCol() {
    return createDiv('col');
}

function createCard(cardId, question, points) {
    let card = createDiv('card', cardId);
    let body = createDiv('card-body', `${cardId}-body`);

    let cardTitle = createElement('h5', 'card-title', '', question);
    card.appendChild(cardTitle);

    let cardSubtitle = createElement('h6', 'card-subtitle mb-2 text-muted', '', `${points}/choice`);
    card.appendChild(cardSubtitle);

    let addQuestion = createElement('button', 'btn btn-success', '', '+');
    addQuestion.onclick = () => addQuestionToCard(cardId);

    body.appendChild(addQuestion);

    card.appendChild(body);
    return card;
}

function addQuestionToCard(cardId) {
    let card = document.getElementById(`${cardId}-body`);

    let inputId = `${cardId}-input-${(new Date).getTime()}`;

    let inputDiv = createElement('div', 'input-group', inputId);
    let input = createElement('input', 'form-control', '', '', {'placeholder': 'Choice'});
    inputDiv.appendChild(input);

    let span = createElement('span', 'input-group-button');
    let removeQuestion = createElement('button', 'btn btn-danger', '', '-');
    removeQuestion.onclick = () => removeQuestionFromCard(inputId);
    span.appendChild(removeQuestion);
    inputDiv.appendChild(span);

    card.appendChild(inputDiv);

    addChoiceToQuestion(cardId, inputId, 'test');
}

function removeQuestionFromCard(questionId) {
    let q = document.getElementById(questionId);
    let parentId = q.parentElement.parentElement.id;
    q.remove();

    removeChoiceFromQuestion(parentId, questionId);
}

function addShortQuestion() {
    let id = (new Date).getTime();
    let questionInput = document.getElementById('question-input');
    let question = questionInput.value;
    questionInput.value = '';

    let pointsInput = document.getElementById('points-input');
    let points = pointsInput.value;
    pointsInput.value = 1;

    document.getElementById('form').appendChild(createCard(id, question, points));
    addQuestionToTemplate(id, 'short', question, points);
}

function addMediumQuestion() {
    console.log('test')
}

function addLongQuestion() {
    console.log('test')
}

function addTableQuestion() {
    console.log('test')
}