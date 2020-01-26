import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train/255.0
x_test = x_test/255.0

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())  # Convert a multidimensional tensor into a single 1-D tensor
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# It trains the model by  repeatedly iterating over the entire dataset for a given number of "epochs"
model.fit(x_train, y_train, epochs=3)

test_loss, test_acc = model.evaluate(x_test, y_test)
print(test_acc)

model.save("model.h5")  # Saving the Model
