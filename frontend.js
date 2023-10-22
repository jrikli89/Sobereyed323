/**
 * @file This file handles all user interaction events on the new frontend elements.
 */

// Helper function abstracting the repetitive logic for adding event listeners and calling backend API
function setupEventListener(elementClass, callback) {
    document.querySelector(`.${elementClass}`).addEventListener('click', callback);
}

// Error handling function
function handleErrors(response) {
    if (!response.ok) throw Error(response.statusText);
    return response;
}

// Callback functions calling the corresponding backend API and handling loading and errors
const actionElement1 = () => {
    document.body.classList.add('loading');
    fetch('/api/element1').catch(handleErrors).then(() => document.body.classList.remove('loading'));
};

const actionElement2 = () => {
    document.body.classList.add('loading');
    fetch('/api/element2').catch(handleErrors).then(() => document.body.classList.remove('loading'));
};

const actionElement3 = () => {
    document.body.classList.add('loading');
    fetch('/api/element3').catch(handleErrors).then(() => document.body.classList.remove('loading'));
};

const actionNewFeature = () => {
    document.body.classList.add('loading');
    fetch('/api/new_feature').catch(handleErrors).then(() => document.body.classList.remove('loading'));
};

const actionAnotherNewFeature = () => {
    document.body.classList.add('loading');
    fetch('/api/another_new_feature').catch(handleErrors).then(() => document.body.classList.remove('loading'));
};

// Add event listeners to new elements on the watch page
setupEventListener('new-front-end-element1', actionElement1);
setupEventListener('new-front-end-element2', actionElement2);
setupEventListener('new-front-end-element3', actionElement3);
setupEventListener('new_feature', actionNewFeature);
setupEventListener('another_new_feature', actionAnotherNewFeature);