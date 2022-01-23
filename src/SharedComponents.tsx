import LoadingOverlay from 'react-loading-overlay';
import styled from 'styled-components/macro';

const UnlockButtonContainer = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: center;
  padding: 20px;
`;

const UnlockButton = styled.button`
  background-color: transparent;
  padding: 5px;
  border: 0px;
`;

const PageContainer = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: center;
  background-color: rgb(19, 58, 79);
  width: 100%;
  height: 100%;
`;

const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  max-width: 350px;
  height: 100%;
  overflow-y: scroll;
  padding: 0px 0px 50px;
  box-sizing: border-box;
`;

const Spinner = styled.img`
  color: blue;
  padding: 48px 0 0 0;
  height: 70px;
`;

const StyledForm = styled.form``;

const BodyP = styled.p`
  font-size: 16px;
  margin: 5px;
  text-align: center;
  color: rgb(209, 209, 209);

  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans',
    'Droid Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
`;

const ErrorP = styled(BodyP)`
  color: rgb(230, 92, 92);
`;

const TitleP = styled.p`
  font-size: 20px;
  margin: 80px 0px 40px;
  color: rgb(209, 209, 209);
  text-align: center;

  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans',
    'Droid Sans', 'Helvetica Neue', sans-serif;
  font-weight: 500;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
`;

const PasscodeInputContainer = styled.div`
  padding: 5px 100px;
`;

const PasscodeInput = styled.input`
  background-color: rgb(118, 147, 182);
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New', monospace;
  font-size: 20px;
  width: 100%;
  box-sizing: border-box;
  padding: 5px;
  /* margin: 5px; */
`;

const StyledLoadingOverlay = styled(LoadingOverlay)`
  display: flex;
  flex-direction: column;
  justify-content: center;
  .Loader_overlay {
    background: rgba(0, 0, 0, 0);
  }
  &.Loader_wrapper--active {
    overflow: hidden;
  }
`;

const LockIconImg = styled.img`
  height: 120px;
  pointer-events: none;
`;

export {
  UnlockButton,
  BodyP,
  PasscodeInput,
  StyledLoadingOverlay,
  PageContainer,
  AppContainer,
  StyledForm,
  LockIconImg,
  Spinner,
  UnlockButtonContainer,
  PasscodeInputContainer,
  TitleP,
  ErrorP,
};
