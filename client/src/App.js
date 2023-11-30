import './App.css';
import Home from './pages/Home';
import Landing from './pages/Landing';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          {/* <Route exact path='/' element={<Landing />} /> */}
          <Route exact path='/' element={<Home />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
