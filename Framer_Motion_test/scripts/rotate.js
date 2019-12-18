<script crossorigin src="https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.23/browser.min.js"></script>
<script src="https://unpkg.com/browse/framer-motion@1.7.0/dist/framer-motion.js"></script>

const styles = {
  background: "blue",
  borderRadius: 30,
  width: 150,
  height: 150,
  margin: "auto"
};

export const Rotate = () => (
  <motion.div
    style={styles}
    animate={{ rotate: 360 }}
    transition={{ duration: 2 }}
  />
);
