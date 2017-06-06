from mock import mock,Mock
#https://stackoverflow.com/questions/16162015/mocking-python-function-based-on-input-arguments #very good examples


mock = MagicMock(side_effect=[4, 5, 6])
print mock()
print mock()
print mock()
mock = Mock(side_effect=Exception('Boom!'))
print mock()
