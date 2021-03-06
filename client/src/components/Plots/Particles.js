import Particles from "react-tsparticles";
import "./Particles.css"

const ParticlesLoader = () => {
    const particlesInit = (main) => {
      console.log(main);
  
      // you can initialize the tsParticles instance (main) here, adding custom shapes or presets
    };
  
    const particlesLoaded = (container) => {
      console.log(container);
    };
    return (
      <div id="particles">
      <Particles
        id="tsparticles"
        init={particlesInit}
        loaded={particlesLoaded}
        options={{
          background: {
            color: {
              value: "#121212"
            },
          },
          fpsLimit: 180,
          interactivity: {
            events: {
              onClick: {
                enable: true,
                mode: "push",
              },
              onHover: {
                enable: true,
                mode: "repulse",
              },
              resize: false,
            },
            modes: {
              bubble: {
                distance: 400,
                duration: 2,
                opacity: 0.8,
                size: 5,
              },
              push: {
                quantity: 0,
              },
              repulse: {
                distance: 200,
                duration: 0.4,
              },
            },
          },
          particles: {
            color: {
              value: "#ffffff",
            },
            links: {
              color: "#ffffff",
              distance: 150,
              enable: true,
              opacity: 0.5,
              width: 1,
            },
            collisions: {
              enable: true,
            },
            move: {
              direction: "none",
              enable: true,
              outMode: "bounce",
              random: false,
              speed: 1,
              straight: false,
            },
            number: {
              density: {
                enable: true,
                value_area: 800,
              },
              value: 15,
            },
            opacity: {
              value: 0.5,
            },
            shape: {
              type: "circle",
            },
            size: {
              random: false,
              value: 5,
            },
          },
          detectRetina: true,
        }}
      /></div>
    );
};

export default ParticlesLoader;
