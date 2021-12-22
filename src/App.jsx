import React, { useState } from 'react';
import './App.css';
import lockFailed from './lock-failed.svg';
import lockUnlocked from './lock-unlocked.svg';
import lock from './lock.svg';

const renderResult = ({ success }) =>
  success ? (
    <img src={lockUnlocked} className="Lock-icon" alt="lock" />
  ) : (
    <img src={lockFailed} className="Lock-icon" alt="lock" />
  );

const App = function () {
  const [requested, setRequested] = useState(false);
  const [success, setSuccess] = useState();

  const handleClickLock = () => {
    fetch(`/api/unlock/${1}`)
      // .then((res) => {
      //   console.log(res);
      //   return res;
      // })
      .then((res) => res.json())
      .then((data) => {
        console.log({ data });
        setSuccess(data.success);
        setRequested(true);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        {requested ? (
          renderResult({ success })
        ) : (
          <div onClick={handleClickLock} role="button" tabIndex={0} onKeyPress={handleClickLock}>
            <img src={lock} className="Lock-icon" alt="lock" />
          </div>
        )}
        <p>tap to unlock</p>
      </header>
    </div>
  );
};

export default App;
